# Test data
session1_attendees = ["Alice", "Bob", "Charlie"]
session2_attendees = ["Charlie", "David", "Alice"]
session3_attendees = ["Eve", "Frank", "Alice"]

conference_session = {
    "Session 1": session1_attendees,
    "Session 2": session2_attendees,
    "Session 3": session3_attendees
}

# Finding unique attendees
unique_attendees_set = set()

for session_name, attendees_list in conference_session.items() :
  current_session_set = set(attendees_list)

  # Print attendees for current session
  print(f"👥 {session_name} attendees: {', '.join(attendees_list)}")

  unique_attendees_set = unique_attendees_set.union(current_session_set)

total_unique_attendees = len(unique_attendees_set)

# Output
print("\n🎯 Results")
print("-" * 30)
print(f"Unique participants across all sessions: {', '.join(sorted(list(unique_attendees_set)))}")
print(f"Total unique participants: {total_unique_attendees}")
