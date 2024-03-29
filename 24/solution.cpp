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
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;
        ListNode* prv = new ListNode(0, head);
        ListNode* nxt = head->next;
        head = head->next;
        while(nxt != NULL){
            prv->next->next = nxt->next;
            nxt->next = prv->next;
            prv->next = nxt;
            if(nxt->next->next != NULL){
                prv = nxt->next;
                nxt = nxt->next->next->next;
            }else break;
        }
        return head;
    }
};
