import json

def combine_lists(list1, list2):
    """
    Combines two lists of elements based on position overlap.
    If more than half of one element is contained within another, their values are merged.
    """
    # Sort all elements by their left position
    combined_elements = sorted(list1 + list2, key=lambda item: item['positions'][0])
    merged_result = []

    for current_element in combined_elements:
        has_merged = False
        for existing_element in merged_result:
            left1, right1 = existing_element['positions']
            left2, right2 = current_element['positions']
            
            # Calculate overlap between current and existing element
            overlap_length = max(0, min(right1, right2) - max(left1, left2))
            current_length = right2 - left2
            
            # Merge if overlap is more than half of current element
            if overlap_length > current_length / 2:
                existing_element['values'].extend(current_element['values'])
                # Remove duplicates while preserving order
                existing_element['values'] = list(dict.fromkeys(existing_element['values']))
                has_merged = True
                break
        
        # If not merged, add as new element
        if not has_merged:
            merged_result.append(current_element)

    return merged_result

# --- Input from user ---
try:
    print("Enter first list in JSON format:")
    list1_input = input()
    list1 = json.loads(list1_input)

    print("\nEnter second list in JSON format:")
    list2_input = input()
    list2 = json.loads(list2_input)

    result = combine_lists(list1, list2)
    print("\nCombined List based on overlapping positions:")
    print(json.dumps(result, indent=2))

except json.JSONDecodeError:
    print("Invalid input. Please enter lists in correct JSON format.")
