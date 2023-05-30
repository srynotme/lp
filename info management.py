# Define Knowledge Base
knowledge_base = {
    'Document Management': {
        'Benefits': ['Centralized storage', 'Easy retrieval', 'Version control'],
        'Challenges': ['Data security', 'Document organization', 'Collaboration'],
        'Best Practices': ['Use naming conventions', 'Implement access controls', 'Regular backups']
    },
    'Data Backup': {
        'Benefits': ['Data protection', 'Disaster recovery', 'Business continuity'],
        'Challenges': ['Data storage capacity', 'Data transfer speed', 'Data integrity'],
        'Best Practices': ['Automate backup process', 'Store backups offsite', 'Test backup restoration']
    },
    'Information Security': {
        'Benefits': ['Data confidentiality', 'Data integrity', 'Data availability'],
        'Challenges': ['Security breaches', 'Vulnerabilities', 'User awareness'],
        'Best Practices': ['Use strong passwords', 'Implement encryption', 'Regular security audits']
    }
}

# Get User Input
topic = input("Enter the information management topic you want to explore: ")

# Check if Topic Exists in Knowledge Base
if topic in knowledge_base:
    # Retrieve Information for the Topic
    topic_info = knowledge_base[topic]

    # Print Benefits
    print(f"Benefits of {topic}:")
    for benefit in topic_info['Benefits']:
        print("- " + benefit)

    # Print Challenges
    print(f"Challenges of {topic}:")
    for challenge in topic_info['Challenges']:
        print("- " + challenge)

    # Print Best Practices
    print(f"Best Practices for {topic}:")
    for practice in topic_info['Best Practices']:
        print("- " + practice)
else:
    print("Topic not found in the knowledge base. Please enter a valid topic.")

