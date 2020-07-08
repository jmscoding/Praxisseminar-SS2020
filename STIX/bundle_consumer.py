from bundle_creator import bundle
import re

# Consumer
for obj in bundle.objects:
    if obj == threat_actor:
        print("------------------")
        print("== THREAT ACTOR ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Threat Actor Types: " + str(obj.threat_actor_types))
        print("Roles: " + str(obj.roles))
        print("Goals: " + str(obj.goals))
        print("Sophistication: " + obj.sophistication)
        print("Resource Level: " + obj.resource_level)
        print("Primary Motivation: " + obj.primary_motivation)
        print("Secondary Motivations: " + str(obj.secondary_motivations))

    elif obj == identity1:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Identity Class: " + obj.identity_class)

    elif obj == identity2:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Identity Class: " + obj.identity_class)

    elif obj == attack_pattern1:
        print("------------------")
        print("== ATTACK PATTERN ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Type: " + obj.type)
        print("External References: " + str(obj.external_references))

    elif re.search('relationship*', str(obj)):
        print("------------------")
        print("== RELATIONSHIP ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Type: " + obj.type)
        print("Relationship Type: " + obj.relationship_type)
        print("Source Ref: " + obj.source_ref)
        print("Target Ref: " + obj.target_ref)
