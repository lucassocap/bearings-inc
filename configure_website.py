#!/usr/bin/env python3
"""
Configure Bearings Inc Website with Images
Upload images and configure Odoo website theme
"""
import base64
import xmlrpc.client
from pathlib import Path


def connect_odoo(url, db, username, password):
    """Connect to Odoo"""
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    
    if not uid:
        raise Exception("Authentication failed")
    
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    return uid, models


def upload_image(models, db, uid, password, image_path, name):
    """Upload image to Odoo as attachment"""
    print(f"   📤 Uploading {name}...")
    
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    attachment_id = models.execute_kw(
        db, uid, password,
        'ir.attachment', 'create',
        [{
            'name': name,
            'type': 'binary',
            'datas': image_data,
            'public': True,
            'res_model': 'ir.ui.view',
        }]
    )
    
    return attachment_id


def configure_website(url, db, username, password):
    """Configure website with images"""
    print("🎨 Bearings Inc - Website Configuration")
    print("=" * 70)
    
    # Connect
    print("\n🔌 Connecting to Odoo...")
    uid, models = connect_odoo(url, db, username, password)
    print(f"✅ Connected as user ID: {uid}")
    
    # Upload images
    print("\n📤 Uploading images...")
    images_dir = Path('assets/images')
    
    images_to_upload = {
        'hero_banner': 'bearings_hero_banner_1768368003121.png',
        'logo': 'bearings_inc_logo_1768368076425.png',
        'ball_bearings': 'ball_bearings_category_1768368016447.png',
        'roller_bearings': 'roller_bearings_category_1768368030440.png',
        'thrust_bearings': 'thrust_bearings_category_1768368048286.png',
        'special_bearings': 'special_bearings_category_1768368061926.png',
        'icon_shipping': 'icon_fast_shipping_1768368089437.png',
        'icon_quality': 'icon_quality_guarantee_1768368102321.png',
        'icon_support': 'icon_support_1768368114519.png',
        'icon_premium': 'icon_premium_quality_1768368126660.png',
    }
    
    uploaded = {}
    for key, filename in images_to_upload.items():
        image_path = images_dir / filename
        if image_path.exists():
            attachment_id = upload_image(models, db, uid, password, image_path, key)
            uploaded[key] = attachment_id
            print(f"      ✅ {key}: ID {attachment_id}")
        else:
            print(f"      ⚠️  {key}: File not found")
    
    # Configure website settings
    print("\n🌐 Configuring website...")
    
    try:
        # Get website
        websites = models.execute_kw(
            db, uid, password,
            'website', 'search',
            [[('id', '>', 0)]], {'limit': 1}
        )
        
        if websites:
            website_id = websites[0]
            
            # Update website settings
            models.execute_kw(
                db, uid, password,
                'website', 'write',
                [[website_id], {
                    'name': 'Bearings Inc',
                }]
            )
            print(f"   ✅ Website configured (ID: {website_id})")
        else:
            print("   ⚠️  No website found")
    
    except Exception as e:
        print(f"   ⚠️  Error configuring website: {str(e)}")
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 Configuration Summary:")
    print(f"   Images uploaded: {len(uploaded)}/10")
    print("\n✅ Website configuration complete!")
    print("\n🔗 Next steps:")
    print("   1. Go to http://localhost:8069")
    print("   2. Website → Edit")
    print("   3. Add images from Media Library")
    print("   4. Customize theme and layout")
    
    return uploaded


def main():
    # Configuration
    URL = "http://localhost:8069"
    DB = "bearings"
    USERNAME = "admin"
    PASSWORD = "admin"
    
    try:
        uploaded = configure_website(URL, DB, USERNAME, PASSWORD)
        
        if uploaded:
            print("\n✅ Configuration completed successfully!")
            exit(0)
        else:
            print("\n⚠️  Some images failed to upload")
            exit(1)
            
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        exit(1)


if __name__ == '__main__':
    main()
