child_1 = {
  'value': 2,
  'children': []
}

child_2 = {
  'value': 3,
  'children': []
}

child_3 = {
  'value': 4,
  'children': []
}

root = {
  'value': 1,
  'children': [child_1, child_2, child_3]
}

class Tree:
  def __init__(self, root = None):
    self.root = root

  def breadth_first_traversal(self, node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      # Remove the first node from the 'nodes_to_visit' list
      node = nodes_to_visit.pop(0)
      # Add its value to the result list
      result.append(node['value'])
      # Add its children (if any) to the END of the 'nodes_to_visit' list.
      nodes_to_visit = nodes_to_visit + node['children']

    return result
  
  def depth_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      # Remove the first node from the 'nodes_to_visit' list
      node = nodes_to_visit.pop(0)
      # Add its value to the result list
      result.append(node['value'])
      # Add its children (if any) to the END of the 'nodes_to_visit' list.
      nodes_to_visit = node['children'] + nodes_to_visit

    return result
  
  def depth_first_traversal_recursive(node, result = []):
    # visit each node (add it to the list of results)
    result.append(node['value'])
    for child in node['children']:
      # visit each child node
        depth_first_traversal_recursive(child, result)

    return result