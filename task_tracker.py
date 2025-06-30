#!/usr/bin/env python3
"""
Tesphase Task Tracker
Simple tool to log your daily progress on Tesphase startup tasks
"""

import json
import os
from datetime import datetime, date
from typing import List, Dict

class TesphaseTaskTracker:
    def __init__(self):
        self.tasks_file = 'tesphase_tasks.json'
        self.load_tasks()
        
        # Predefined task categories for Tesphase
        self.task_categories = {
            'solar_research': '🔋 Solar Panel Research',
            'innovation': '💡 Renewable Energy Innovation', 
            'environmental': '🌍 Environmental Impact Analysis',
            'market_research': '📊 Market Research & Analysis',
            'partnerships': '🤝 Partnership Development',
            'funding': '💰 Funding & Investor Outreach',
            'product_dev': '⚙️ Product Development',
            'marketing': '📢 Marketing & Branding',
            'operations': '🏢 Operations & Logistics',
            'other': '📝 Other Tasks'
        }

    def load_tasks(self):
        """Load existing tasks from file."""
        try:
            if os.path.exists(self.tasks_file):
                with open(self.tasks_file, 'r') as f:
                    self.tasks = json.load(f)
            else:
                self.tasks = {
                    'start_date': datetime.now().strftime('%Y-%m-%d'),
                    'daily_tasks': {},
                    'milestones': [],
                    'total_hours': 0
                }
                self.save_tasks()
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = {
                'start_date': datetime.now().strftime('%Y-%m-%d'),
                'daily_tasks': {},
                'milestones': [],
                'total_hours': 0
            }

    def save_tasks(self):
        """Save tasks to file."""
        try:
            with open(self.tasks_file, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, category: str, description: str, hours: float = 0):
        """Add a new task for today."""
        today = date.today().strftime('%Y-%m-%d')
        
        if today not in self.tasks['daily_tasks']:
            self.tasks['daily_tasks'][today] = []
        
        task = {
            'id': len(self.tasks['daily_tasks'][today]) + 1,
            'category': category,
            'description': description,
            'hours': hours,
            'completed': False,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.tasks['daily_tasks'][today].append(task)
        self.tasks['total_hours'] += hours
        self.save_tasks()
        
        print(f"✅ Task added: {self.task_categories.get(category, category)} - {description}")

    def complete_task(self, task_id: int):
        """Mark a task as completed."""
        today = date.today().strftime('%Y-%m-%d')
        
        if today in self.tasks['daily_tasks']:
            for task in self.tasks['daily_tasks'][today]:
                if task['id'] == task_id:
                    task['completed'] = True
                    task['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    self.save_tasks()
                    print(f"🎉 Task completed: {task['description']}")
                    return
        
        print("❌ Task not found")

    def show_today_tasks(self):
        """Display today's tasks."""
        today = date.today().strftime('%Y-%m-%d')
        
        print(f"\n🌞 Tesphase Tasks for {today} 🌞")
        print("=" * 50)
        
        if today not in self.tasks['daily_tasks'] or not self.tasks['daily_tasks'][today]:
            print("No tasks logged for today yet!")
            print("\n💡 Suggested focus areas:")
            for category, name in self.task_categories.items():
                print(f"  • {name}")
            return
        
        total_hours = 0
        completed_tasks = 0
        
        for task in self.tasks['daily_tasks'][today]:
            status = "✅" if task['completed'] else "⏳"
            category_name = self.task_categories.get(task['category'], task['category'])
            print(f"{status} [{task['id']}] {category_name}")
            print(f"    {task['description']}")
            if task['hours'] > 0:
                print(f"    ⏱️  {task['hours']} hours")
            print()
            
            total_hours += task['hours']
            if task['completed']:
                completed_tasks += 1
        
        print(f"📊 Summary: {completed_tasks}/{len(self.tasks['daily_tasks'][today])} tasks completed")
        print(f"⏱️  Total hours today: {total_hours}")

    def show_categories(self):
        """Show available task categories."""
        print("\n📋 Available Task Categories:")
        print("=" * 30)
        for key, name in self.task_categories.items():
            print(f"  {key}: {name}")

    def add_milestone(self, title: str, description: str):
        """Add a milestone achievement."""
        milestone = {
            'id': len(self.tasks['milestones']) + 1,
            'title': title,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.tasks['milestones'].append(milestone)
        self.save_tasks()
        
        print(f"🏆 Milestone added: {title}")

    def show_milestones(self):
        """Show all milestones."""
        print(f"\n🏆 Tesphase Milestones ({len(self.tasks['milestones'])} total)")
        print("=" * 40)
        
        if not self.tasks['milestones']:
            print("No milestones yet. Keep working on Tesphase!")
            return
        
        for milestone in self.tasks['milestones']:
            print(f"🏆 {milestone['title']}")
            print(f"   {milestone['description']}")
            print(f"   📅 {milestone['date']}")
            print()

    def show_stats(self):
        """Show overall statistics."""
        total_tasks = 0
        total_completed = 0
        
        for day_tasks in self.tasks['daily_tasks'].values():
            total_tasks += len(day_tasks)
            total_completed += sum(1 for task in day_tasks if task['completed'])
        
        print(f"\n📊 Tesphase Progress Statistics")
        print("=" * 35)
        print(f"📅 Started: {self.tasks['start_date']}")
        print(f"📝 Total tasks: {total_tasks}")
        print(f"✅ Completed tasks: {total_completed}")
        print(f"⏱️  Total hours logged: {self.tasks['total_hours']}")
        print(f"🏆 Milestones: {len(self.tasks['milestones'])}")
        
        if total_tasks > 0:
            completion_rate = (total_completed / total_tasks) * 100
            print(f"📈 Completion rate: {completion_rate:.1f}%")

def main():
    """Main function for the task tracker."""
    tracker = TesphaseTaskTracker()
    
    print("🌞 Welcome to Tesphase Task Tracker! 🌞")
    print("Track your daily progress on your solar energy startup")
    
    while True:
        print("\n" + "=" * 50)
        print("📋 Menu:")
        print("1. Add task")
        print("2. Complete task")
        print("3. Show today's tasks")
        print("4. Show categories")
        print("5. Add milestone")
        print("6. Show milestones")
        print("7. Show statistics")
        print("8. Exit")
        
        choice = input("\nChoose an option (1-8): ").strip()
        
        if choice == '1':
            tracker.show_categories()
            category = input("Enter category (or key): ").strip()
            description = input("Enter task description: ").strip()
            hours = input("Enter hours spent (0 if none): ").strip()
            
            try:
                hours = float(hours) if hours else 0
            except ValueError:
                hours = 0
            
            tracker.add_task(category, description, hours)
            
        elif choice == '2':
            tracker.show_today_tasks()
            task_id = input("Enter task ID to complete: ").strip()
            try:
                tracker.complete_task(int(task_id))
            except ValueError:
                print("❌ Invalid task ID")
                
        elif choice == '3':
            tracker.show_today_tasks()
            
        elif choice == '4':
            tracker.show_categories()
            
        elif choice == '5':
            title = input("Enter milestone title: ").strip()
            description = input("Enter milestone description: ").strip()
            tracker.add_milestone(title, description)
            
        elif choice == '6':
            tracker.show_milestones()
            
        elif choice == '7':
            tracker.show_stats()
            
        elif choice == '8':
            print("👋 Keep working on Tesphase! Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 