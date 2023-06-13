/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        int size=0;
        ListNode* cur = head;
        while(cur){
            size++;
            cur = cur->next;
        }
        return mergeSort(head, size);
    }
    ListNode* mergeSort(ListNode* left, int size){
        if(left == NULL) return NULL;
        if(left->next == NULL) return left;
        ListNode* right = left;
        int new_size = (size-1)/2;
        int cnt = new_size;
        while(cnt--){
           right = right->next; 
        }
        ListNode* temp = right->next;
        right->next = NULL;
        right = temp;
        // cout<<left->val<<" "<<right->val<<"\n";

        left = mergeSort(left, new_size+1);
        right = mergeSort(right, size-new_size-1);
        ListNode head(0);
        ListNode* cur = &head;
        while(true){
            if(left && right){
                if(left->val < right->val){
                    cur->next = left;
                    left = left->next;
                    cur = cur->next;
                }else{
                    cur->next = right;
                    right = right->next;
                    cur = cur->next;
                }
            }else if(left){
                cur->next = left;
                break;
            }else{
                cur->next = right;
                break;
            }
        }
        return (&head)->next;
    }
};
