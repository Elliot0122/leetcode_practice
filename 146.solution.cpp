class LRUCache {
public:
    LRUCache(int capacity_) {
        cacheSize = capacity_;
    }
    
    int get(int key) {
        if(map.find(key)==map.end()){
            return -1;
        }
        LRU.splice(LRU.begin(), LRU, map[key]);
        return map[key]->second;
    }
    
    void put(int key, int value) {
        if(map.find(key)!=map.end()){
            LRU.splice(LRU.begin(), LRU, map[key]);
            map[key]->second = value;
            return;
        }
        if(used == cacheSize){
            int L_key = LRU.back().first;
            LRU.pop_back();
            map.erase(L_key);
            used--;
        }
        used++;
        LRU.push_front({key, value});
        map[key] = LRU.begin();
    }
private:
    unordered_map<int, list<pair<int,int>>::iterator> map;
    list<pair<int,int>> LRU;
    int used = 0;
    int cacheSize = 0;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
