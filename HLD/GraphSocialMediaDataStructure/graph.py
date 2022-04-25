
class Person:
    
    def __init__(self, id, name, friend_ids):
        self.id = id
        self.name = name
        self.friend_ids = friend_ids

class PersonServer:
    
    def __init__(self):
        self.person_id_to_person_object_map = {}  # key: person_id, value: person

    def add_person(self, person):
        """Add person_id to server
        """
        self.person_id_to_person_object_map[person.id] = person

    def get_person_object(self, ids):
        """Returns the person present in this server
        """
        results = []
        for id in ids:
            if id in self.person_id_to_person_object_map:
                results.append(self.person_id_to_person_object_map[id])
        return results

class LookupService:
    """
    Track the server of given person
    """
    def __init__(self):
        self.lookup = self._init_lookup()  # key: person_id, value: person_server

    def _init_lookup(self):
        """initialize with Naive values
        """

    def lookup_person_server(self, person_id):
        return self.lookup[person_id]
    
class UserGraphService(object):
    
    def __init__(self, lookup_service):
        self.lookup_service = lookup_service

    def get_person_with_person_id(self, person_id):
        person_server = self.lookup_service.lookup_person_server(person_id)
        return person_server.get_person_object([person_id])

    def shortest_path(self, source_key, dest_key):
        if source_key is None or dest_key is None:
            return None
        if source_key is dest_key:
            return [source_key]
        prev_node_keys = self._shortest_path(source_key, dest_key)
        if prev_node_keys is None:
            return None
        else:
            # Iterate through the path_ids backwards, starting at dest_key
            path_ids = [dest_key]
            prev_node_key = prev_node_keys[dest_key]
            while prev_node_key is not None:
                path_ids.append(prev_node_key)
                prev_node_key = prev_node_keys[prev_node_key]
            # Reverse the list since we iterated backwards
            return path_ids[::-1]

    def _shortest_path(self, source_key, dest_key, path):
        # Use the id to get the Person
        source = self.get_person_with_person_id(source_key)
        # Update our bfs queue
        from collections import deque
        queue = deque()
        queue.append(source)
        # prev_node_keys keeps track of each hop from
        # the source_key to the dest_key
        prev_node_keys = {source_key: None}
        # We'll use visited_ids to keep track of which nodes we've
        # visited, which can be different from a typical bfs where
        # this can be stored in the node itself
        visited_ids = set()
        visited_ids.add(source.id)
        while queue:
            node = queue.popleft()
            if node.key is dest_key:
                return prev_node_keys
            prev_node = node
            for friend_id in node.friend_ids:
                if friend_id not in visited_ids:
                    friend_node = self.get_person_with_person_id(friend_id)
                    queue.append(friend_node)
                    prev_node_keys[friend_id] = prev_node.key
                    visited_ids.add(friend_id)
        return None