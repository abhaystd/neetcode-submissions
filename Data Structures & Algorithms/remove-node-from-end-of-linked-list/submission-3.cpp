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
        if (!head){
            return NULL;
        }

        int l=0;
        ListNode * temp=head;
        while(temp){
            temp=temp->next;
            l++;
        }

        if (n==l){
            return head->next;
        }

        ListNode* prev=NULL;
        temp=head;
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
