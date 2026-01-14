#!/usr/bin/env python3
"""
Fix Bearings Inc Website - Direct Database Approach
Edits website content directly in Odoo database
"""
import xmlrpc.client


def connect_odoo(url, db, username, password):
    """Connect to Odoo"""
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    
    if not uid:
        raise Exception("Authentication failed")
    
    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
    return uid, models


def fix_website(url, db, username, password):
    """Fix website content"""
    print("🔧 Bearings Inc - Automated Website Fixes")
    print("=" * 70)
    
    # Connect
    print("\n🔌 Connecting to Odoo...")
    uid, models = connect_odoo(url, db, username, password)
    print(f"✅ Connected as user ID: {uid}")
    
    fixes_applied = []
    
    # 1. Update website pages (ir.ui.view)
    print("\n📄 Fixing website pages...")
    
    try:
        # Find homepage view
        view_ids = models.execute_kw(
            db, uid, password,
            'ir.ui.view', 'search',
            [[('type', '=', 'qweb'), ('website_id', '!=', False)]],
            {'limit': 50}
        )
        
        if view_ids:
            views = models.execute_kw(
                db, uid, password,
                'ir.ui.view', 'read',
                [view_ids],
                {'fields': ['id', 'name', 'arch_db']}
            )
            
            for view in views:
                arch = view.get('arch_db', '')
                updated = False
                
                # Replace placeholder email
                if 'hello@mycompany.com' in arch:
                    arch = arch.replace('hello@mycompany.com', 'sales@bearingsinc.com')
                    updated = True
                
                # Replace placeholder phone
                if '+1 555-555-5556' in arch:
                    arch = arch.replace('+1 555-555-5556', '+1 (555) 123-4567')
                    updated = True
                
                # Update if changed
                if updated:
                    models.execute_kw(
                        db, uid, password,
                        'ir.ui.view', 'write',
                        [[view['id']], {'arch_db': arch}]
                    )
                    fixes_applied.append(f"Updated view: {view['name']}")
                    print(f"   ✅ Updated: {view['name']}")
        
    except Exception as e:
        print(f"   ⚠️  Error updating views: {str(e)}")
    
    # 2. Update website configuration
    print("\n🌐 Updating website configuration...")
    
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
                    'company_id': 1,
                }]
            )
            fixes_applied.append("Updated website name")
            print(f"   ✅ Website name updated")
    
    except Exception as e:
        print(f"   ⚠️  Error updating website: {str(e)}")
    
    # 3. Publish products to website
    print("\n🛍️  Publishing products to website...")
    
    try:
        # Get all products
        product_ids = models.execute_kw(
            db, uid, password,
            'product.template', 'search',
            [[('id', '>', 0)]]
        )
        
        if product_ids:
            # Publish all products
            models.execute_kw(
                db, uid, password,
                'product.template', 'write',
                [product_ids, {'website_published': True}]
            )
            fixes_applied.append(f"Published {len(product_ids)} products")
            print(f"   ✅ Published {len(product_ids)} products to website")
    
    except Exception as e:
        print(f"   ⚠️  Error publishing products: {str(e)}")
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 Fixes Applied:")
    for fix in fixes_applied:
        print(f"   ✅ {fix}")
    
    print(f"\n✅ Total fixes: {len(fixes_applied)}")
    
    print("\n🔗 View your website:")
    print(f"   Homepage: {url}")
    print(f"   Shop: {url}/shop")
    
    print("\n💡 Remaining manual steps:")
    print("   1. Go to Website → Edit")
    print("   2. Replace hero image with ID 878")
    print("   3. Add logo (ID 879) to navbar")
    print("   4. Add feature icons (IDs 884-887)")
    
    return fixes_applied


def main():
    """Main function"""
    URL = "http://localhost:8069"
    DB = "bearings"
    USERNAME = "admin"
    PASSWORD = "admin"
    
    try:
        fixes = fix_website(URL, DB, USERNAME, PASSWORD)
        
        if fixes:
            print("\n✅ Website fixes completed successfully!")
            exit(0)
        else:
            print("\n⚠️  No fixes applied")
            exit(1)
            
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()
