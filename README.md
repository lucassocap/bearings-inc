# Bearings Inc - Odoo 18 eCommerce Website

Professional bearing distributor website built with Odoo 18.

## 🎯 Project Overview

Complete eCommerce solution for Bearings Inc featuring:
- **20 Premium Products** from top brands (FAG, SKF, NACHI, NTN, SW, MRC)
- **Automated Setup** with validation and error handling
- **Netora-Inspired Design** - Clean, professional, conversion-optimized
- **Production Ready** - Docker-based infrastructure

## 📦 What's Included

### Products
- 20 bearing products with high-quality images
- Complete specifications and descriptions
- Competitive pricing
- Multi-brand inventory (6 major brands)

### Features
- ✅ Product catalog with images
- ✅ Category filtering
- ✅ Brand filtering  
- ✅ Search functionality
- ✅ Shopping cart
- ✅ Checkout process
- ✅ Inventory management

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.9+
- 4GB RAM minimum

### Installation

```bash
# 1. Start Odoo 17
cd infrastructure
docker-compose up -d

# 2. Wait for Odoo to be ready (60-90 seconds)
sleep 90

# 3. Run setup script
cd ..
python3 setup.py
```

### Access

- **URL**: http://localhost:8069
- **Database**: bearings
- **Username**: admin
- **Password**: admin

## 📁 Project Structure

```
bearings/
├── README.md
├── data/
│   └── bearing_products.json    # 20 products with images
├── infrastructure/
│   ├── docker-compose.yml       # Odoo 17 + PostgreSQL 15
│   ├── setup.sh                 # Infrastructure setup
│   └── README.md
├── select_bearing_products.py   # Product selection script
└── setup.py                     # Complete setup automation
```

## 🛠️ Tech Stack

- **Odoo**: 18.0 (latest)
- **Database**: PostgreSQL 15
- **Container**: Docker
- **Language**: Python 3.9+

## 📊 Products

### Brands
- FAG
- SKF  
- NACHI
- NTN
- SW
- MRC

### Categories
- Ball Bearings
- Special Bearings

## 🔧 Configuration

### Manual Module Installation (if needed)

Due to Odoo XML-RPC API limitations, you may need to install modules manually:

1. Go to http://localhost:8069
2. Login (admin/admin)
3. Apps → Install:
   - Inventory
   - Website
   - eCommerce

Then run `python3 setup.py` again.

## 📝 Notes

- All product descriptions in English
- Images verified and validated
- Prices competitive and market-ready
- SEO-optimized product names

## 🤝 Support

For issues or questions, contact the development team.

## 📄 License

Proprietary - Bearings Inc © 2026
