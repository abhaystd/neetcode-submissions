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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!head or !head->next){
            return NULL;
        }

        int l=1;
        ListNode * slow=head;
        ListNode * fast=head;
        while(fast and fast->next){
            slow=slow->next;
            fast=fast->next->next;
            l++;
        }
        
        if (!fast){
            l=2*l-2;
        }
        else{
            l=2*l-1;
        }
        cout<<l;
        if (n==l){
            return head->next;
        }

        ListNode* prev=NULL;
        ListNode* temp=head;
        int idx = l-n;
        while(idx--){
            prev=temp;
            temp=temp->next;
        }
        ListNode * nodeToDelete=temp;
        prev->next=temp->next;
        delete nodeToDelete;
        // TC O(N) AND SCO(1)
        return head;
    }
};
