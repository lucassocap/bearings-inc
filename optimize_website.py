#!/usr/bin/env python3
"""
Optimize Bearings Inc Website
Uses WebsiteOptimizerAgent to diagnose and fix website
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'odoo' / 'odoo-ai-configurator'))

from src.orchestrator import Orchestrator


def main():
    """Optimize website"""
    print("🔧 Bearings Inc - Website Optimization")
    print("=" * 70)
    
    # Initialize orchestrator
    orchestrator = Orchestrator(
        url="http://localhost:8069",
        db="bearings",
        username="admin",
        password="admin"
    )
    
    # Run optimization
    print("\n🤖 Running WebsiteOptimizerAgent...")
    result = orchestrator.configure("optimize website", {
        'url': 'http://localhost:8069'
    })
    
    print("\n" + "=" * 70)
    print("📊 Optimization Results:")
    print(f"   Status: {result.get('status')}")
    print(f"   Agents executed: {result.get('agents_executed')}")
    
    for agent_result in result.get('results', []):
        print(f"\n   Agent: {agent_result['agent']}")
        agent_data = agent_result['result']
        
        if 'diagnosis' in agent_data:
            diagnosis = agent_data['diagnosis']
            print(f"   Issues found: {diagnosis.get('issues_found', 0)}")
            print(f"   Product count: {diagnosis.get('product_count', 0)}")
        
        if 'fixes_applied' in agent_data:
            fixes = agent_data['fixes_applied']
            print(f"   Fixes applied: {fixes.get('total_fixes', 0)}")
    
    print("\n✅ Optimization complete!")


if __name__ == '__main__':
    main()
