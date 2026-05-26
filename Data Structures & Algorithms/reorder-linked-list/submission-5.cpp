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
    void reorderList(ListNode* head) {
        if (!head or !head->next){
            return;
        }

        ListNode * slow=head;
        ListNode* fast=head;

        while(fast and fast->next){
            slow=slow->next;
            fast=fast->next->next;
        }

        ListNode* second=slow->next;
        slow->next=NULL;
        ListNode* prev=NULL;
        while (second){
            ListNode* nxt=second->next;

            second->next=prev;
            prev=second;

            second = nxt;

        }

        ListNode* first = head;
        second=prev;

        while(second){
            ListNode* nxt1=first->next;
            ListNode* nxt2=second->next;
            
            first->next=second;
            second->next=nxt1;

            second=nxt2;
            first=nxt1;
        }


    }
};
