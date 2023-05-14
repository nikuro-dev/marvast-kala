def group_list(custom_list, size=4):
    """Get a list and returns a 4 item grouped lists."""
    for i in range(0, len(custom_list), size):
        grouped_list = []
        grouped_list.append(custom_list[i:i + size])

        return grouped_list
