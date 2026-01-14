#!/usr/bin/env python3
"""
Diagnose and Optimize Bearings Inc Website
Standalone script - analyzes website and provides recommendations
"""
import requests
from bs4 import BeautifulSoup


def diagnose_website(url):
    """Diagnose website issues"""
    print(f"🔍 Diagnosing website: {url}")
    print("=" * 70)
    
    issues = []
    recommendations = []
    
    try:
        # Fetch homepage
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        print("\n📄 Homepage Analysis:")
        
        # Check title
        title = soup.find('title')
        if title:
            print(f"   Title: {title.text}")
        
        # Check for placeholder text
        text_content = soup.get_text()
        placeholders = {
            'hello@mycompany.com': 'Email placeholder',
            '+1 555-555-5556': 'Phone placeholder',
            'Lorem ipsum': 'Lorem ipsum text',
        }
        
        print("\n⚠️  Issues Found:")
        for placeholder, description in placeholders.items():
            if placeholder.lower() in text_content.lower():
                issues.append(description)
                print(f"   - {description}: {placeholder}")
                recommendations.append(f"Replace {placeholder} with real content")
        
        # Check shop page
        shop_response = requests.get(f'{url}/shop', timeout=10)
        shop_soup = BeautifulSoup(shop_response.content, 'html.parser')
        
        # Count products
        products = shop_soup.find_all('div', class_='oe_product')
        product_count = len(products)
        
        print(f"\n🛍️  Shop Analysis:")
        print(f"   Products found: {product_count}")
        
        if product_count == 0:
            issues.append("No products in shop")
            recommendations.append("Import products to shop")
        
        # Summary
        print("\n" + "=" * 70)
        print(f"📊 Summary:")
        print(f"   Total issues: {len(issues)}")
        print(f"   Products: {product_count}")
        
        if recommendations:
            print(f"\n💡 Recommendations:")
            for i, rec in enumerate(recommendations, 1):
                print(f"   {i}. {rec}")
        
        print("\n✅ Images available in Odoo Media Library:")
        print("   1. Hero Banner (ID 878) - Dramatic industrial scene")
        print("   2. Logo (ID 879) - Professional geometric design")
        print("   3. Ball Bearings (ID 880) - Macro shot")
        print("   4. Roller Bearings (ID 881) - Cinematic angle")
        print("   5. Thrust Bearings (ID 882) - Dramatic lighting")
        print("   6. Special Bearings (ID 883) - Artistic presentation")
        print("   7-10. Feature Icons (IDs 884-887)")
        
        print("\n🔧 To apply images:")
        print("   1. Go to http://localhost:8069")
        print("   2. Website → Edit")
        print("   3. Replace images from Media Library")
        print("   4. Update contact info and placeholder text")
        
        return {
            'issues': len(issues),
            'products': product_count,
            'recommendations': recommendations
        }
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return {'error': str(e)}


def main():
    """Main function"""
    print("🎨 Bearings Inc - Website Diagnosis")
    print("=" * 70)
    
    URL = "http://localhost:8069"
    
    result = diagnose_website(URL)
    
    if 'error' not in result:
        print("\n✅ Diagnosis complete!")
        exit(0)
    else:
        print("\n❌ Diagnosis failed!")
        exit(1)


if __name__ == '__main__':
    main()
