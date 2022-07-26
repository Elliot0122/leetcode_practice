/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if(node == NULL)return NULL;
        unordered_map<Node*, Node*> visited;
        
        return dfs(node, visited);
    }
    Node* dfs(Node* node, unordered_map<Node*, Node*>& visited){
        if(visited.find(node) == visited.end()){
            Node* ans = new Node(node->val);
            visited[node] = ans;
            for(auto nei:node->neighbors)
                ans->neighbors.push_back(dfs(nei, visited));
            return ans;
        }else{
            return visited[node];
        }
    }
};
