class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]
  
    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      elif 'children' in node:
        nodes_to_visit = node['children'] + nodes_to_visit
    
    return None

tree = Tree(
  {
    'tag_name': 'body',
    'id': None,
    'children': [
      {
        'tag_name': 'div',
        'id': 'main',
        'children': [
          {
            'tag_name': 'h1',
            'id': 'heading',
            'text_content': 'Title',
            'children': []
          },
          {
            'tag_name': 'h2',
            'id': None,
            'text_content': 'Subtitle',
            'children': []
          }
        ]
      }
    ]
  }
)

print(tree.get_element_by_id('heading'))