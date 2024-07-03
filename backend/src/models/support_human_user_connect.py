class SupportHumanUserConnect:
    def __init__(self):
        self.user_agent_pairs = {}
        self.agent_user_pairs = {}
        self.connected_support_agents=[]
        self.users_requesting_human_support=[]

    def add_pair(self, user, agent):
        self.user_agent_pairs[user] = agent
        self.agent_user_pairs[agent] = user

    def remove_pair(self, user):
        agent = self.user_agent_pairs.pop(user, None)
        if agent:
            self.agent_user_pairs.pop(agent, None) 

    def get_agent(self, user):
        return self.user_agent_pairs.get(user)
    
    def get_user(self, agent):
        return self.agent_user_pairs.get(agent)
    
    def is_connected(self, user):
        if user in self.user_agent_pairs:
            return True
        elif user in self.agent_user_pairs:
            return True
        else:
            return False
    def support_agent_disconnected(self, sid):
        self.remove_pair(sid)
        
    def user_requesting_human_support(self, sid):
        self.users_requesting_human_support.append(sid)

    def support_agent_connected(self, sid):
        self.connected_support_agents.append(sid)

# class ConnectedPairs:
#     def __init__(self):
#         self.user_agent_pairs = {}
#         self.agent_user_pairs = {}

#     def add_pair(self, user, agent):
#         self.user_agent_pairs[user] = agent
#         self.agent_user_pairs[agent] = user

#     def remove_pair(self, user):
#         agent = self.user_agent_pairs.pop(user, None)
#         if agent:
#             self.agent_user_pairs.pop(agent, None) 

#     def get_agent(self, user):
#         return self.user_agent_pairs.get(user)
    
#     def get_user(self, agent):
#         return self.agent_user_pairs.get(agent)
    
#     def is_connected(self, user):
#         if user in self.user_agent_pairs:
#             return True
#         elif user in self.agent_user_pairs:
#             return True
#         else:
#             return False


# class SupportHumanUserConnect(ConnectedPairs):
#     def __init__(self):
#         super().__init__()
#         self.connected_support_agents=[]
#         self.users_requesting_human_support=[]

#     def connect_user_and_human(self, user_id, human_id):
#         if user_id not in self.users_requesting_human_support or human_id not in self.connected_support_agents:
#             return False
#         else:
#             self.add_pair(user_id, human_id)
#             return True

#     def disconnect_user_and_human(self, disconnector_id):
#         # if the disconnector is a user
#         if self.is_connected(disconnector_id):
#             self.remove_pair(disconnector_id)
#             self.users_requesting_human_support.remove(disconnector_id)
#             return True
#         # if the disconnector is a human
#         elif self.is_connected(disconnector_id):
#             self.remove_pair(disconnector_id)
#             self.connected_support_agents.remove(disconnector_id)
#             return True
#         # not connected at all
#         else:
#             return False

#     def get_connected_human(self, user_id):
#         return self.get_agent(user_id)

#     def get_connected_user(self, human_id):
#         return self.get_user(human_id)
    
#     def support_agent_connected(self, sid, username):
#         # Check if username is already a key in any of the dictionaries in the list
#         if not any(d.get(username) for d in self.connected_support_agents):
#             # If not, append the new username and sid
#             self.connected_support_agents.append({username: sid})
#         else:
#             # If yes, update the sid
#             for d in self.connected_support_agents:
#                 if d.get(username):
#                     d[username] = sid

#     def support_agent_disconnected(self, sid, username):
#         for index, agent_dict in enumerate(self.connected_support_agents):
#             if username in agent_dict:
#                 # Remove the dictionary containing the username and sid
#                 del self.connected_support_agents[index]
#                 break  # Exit the loop after finding and removing the dictionary
#         if self.get_user(sid):
#             self.remove_pair(sid)
        
#     def user_requesting_human_support(self, sid):
#         self.users_requesting_human_support.append(sid)