#!/usr/bin/env python
from social_media_manager.crew import SocialMediaManager
import sys

def run():
    """Main entry point for the crew"""
    print("\n" + "="*70)
    print("BJJ/MMA Personalized DM Generator")
    print("="*70 + "\n")

    athlete_name = input("Enter the name of the fighter/athlete you want to contact: ").strip()
    if not athlete_name:
        print("No name provided. Exiting.")
        sys.exit(0)

    print(f"\nStarting outreach process for: {athlete_name}")
    print("Researching recent accomplishments...")

    # Pass the athlete name + current year to the crew
    inputs = {
        "athlete_name": athlete_name,
        "current_year": "2026"  # or get dynamically: str(datetime.now().year)
    }

    try:
        result = SocialMediaManager().crew().kickoff(inputs=inputs)
        print("\n" + "="*70)
        print("Final Output (Personalized DM):")
        print("-"*70)
        print(result)
        print("="*70 + "\n")
    except Exception as e:
        print(f"Error running crew: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
