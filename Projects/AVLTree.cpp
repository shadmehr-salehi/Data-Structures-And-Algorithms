// Code For Implementing AVL Trees in CPP 
// for more info about avl tree,  visit : https://en.wikipedia.org/wiki/AVL_tree
#include<bits/stdc++.h>
using namespace std;

class Node{
public:
    int data, height;
    Node *right, *left, *par;
    Node(int _v, Node *tmp = nullptr) {
        this->data = _v;
        right = nullptr;
        left = nullptr;
        par = tmp;
        height = 1;
    }
    void push(int);
    void left_rotate();
    void right_rotate();
    void find_height();
    Node* search(int);
    void del(int);
    void print(int);
};

int level(Node *tmp) {
    if (tmp == nullptr)
        return 0;
    return tmp->height;
}

void Node::find_height() {
    this->height = max(level(this->left), level(this->right)) + 1;
    return;
}

int balance_number(Node *tmp) {
    if (tmp == nullptr)
        return 0;
    return level(tmp->right) - level(tmp->left);
}

void balance(Node *tmp) {
    if (tmp->data == INT_MIN || abs(balance_number(tmp)) < 2)
        return;
    // cout << "Balance " << tmp->data << '\n';
    if (balance_number(tmp) > 1) {
        // cout << "In first if'\n";
        if (balance_number(tmp->right) >= 0)
            tmp->left_rotate();
        else {
            tmp->right->right_rotate();
            tmp->left_rotate();
        }
    }
    else {
        // cout << "second if\n";
        if (balance_number(tmp->left) > 0) {
            tmp->left->left_rotate();
            tmp->right_rotate();
        }
        else
            tmp->right_rotate();
    }
    return;
}

void Node::push(int _v) {
    if (this->data < _v) {
        if (this->right == nullptr)
            this->right = new Node(_v, this);
        else
            this->right->push(_v);
    }
    else {
        if (this->left == nullptr)
            this->left = new Node(_v, this);
        else
            this->left->push(_v);
    }
    this->find_height();
    if (abs(level(this->left) - level(this->right)) > 1) 
        balance(this);
    return;
}

void Node::left_rotate() {
    // cout << "Left " << this->data << '\n';
    Node *tmp1 = this->right;
    Node *tmp2 = this->right->left;
    if (this->par != nullptr)
        if (this == this->par->right)
            this->par->right = tmp1;
        else    
            this->par->left = tmp1;
    
    tmp1->left = this;
    this->right = tmp2;

    tmp1->par = this->par;
    if (tmp2 != nullptr)
        tmp2->par = this;
    this->par = tmp1;

    this->find_height();
    tmp1->find_height();
    return;
}

void Node::right_rotate() {
    // cout << "Right " << this->data << '\n';
    Node *tmp1 = this->left;
    Node *tmp2 = this->left->right;

    if (this->par != nullptr)
        if (this == this->par->left)
            this->par->left = tmp1;
        else
            this->par->right = tmp1;
    
    tmp1->right = this;
    this->left = tmp2;

    tmp1->par = this->par;
    this->par = tmp1;
    if (tmp2 != nullptr)
        tmp2->par = this;

    this->find_height();
    tmp1->find_height();
    return;
}

Node* Node::search(int _v) {
    if (this->data == _v)
        return this;
    if (this->data < _v && this->right != nullptr)
        return this->right->search(_v);
    if (this->data > _v && this->left != nullptr)
        return this->left->search(_v);
    return nullptr;
}

void Node::del(int _v) {
    if (this->data < _v)
        this->right->del(_v);
    else if (this->data > _v)
        this->left->del(_v);
    else {
        if (this->left == nullptr && this->right == nullptr) {
            // cout << "Delete first if\n";
            if (this->par->right == this)
                this->par->right = nullptr;
            else
                this->par->left = nullptr;
        }
        else if (this->left == nullptr || this->right == nullptr) {
            // cout << "Delete second if\n";
            if (this->par->right == this)
                this->par->right = (this->left ? this->left : this->right);
            else
                this->par->left = (this->left ? this->left : this->right);
        }
        else {
            // cout << "Delete third if\n";
            Node *tmp = this->right;
            while (tmp->left != nullptr)
                tmp = tmp->left;
            tmp->par->left = tmp->right;
            if (tmp->right != nullptr)
                tmp->right->par = tmp->par;

            Node *tmp2 = tmp->par;
            while(tmp2 != this) {
                tmp2->find_height();
                balance(tmp2);
                tmp2 = tmp2->par;
            }

            tmp->par = this->par;
            tmp->left = this->left;
            tmp->right = this->right;
            if (tmp->right == tmp)
                tmp->right = nullptr;

            if (this->par->right == this)
                this->par->right = tmp;
            else
                this->par->left = tmp;

            tmp->find_height();
            balance(tmp);
        }
        return;
    }
    this->find_height();
    balance(this);
    return;
}

void Node::print(int num) {
    if (this->data != INT_MIN)
        cout << "Num: " << num << ' ' << this->data << '\n';
    if (this->left != nullptr)
        this->left->print(num * 2);
    if (this->right != nullptr)
        this->right->print((num * 2) + 1);
    return;
}

class bst{
private:
    Node *head;
public:
    bst(){
        head = new Node(INT_MIN);
    }
    void push(int _v) {
        head->push(_v);
        return;
    }
    bool search(int _v) {
        return (head->search(_v) != nullptr);
    }
    void del(int _v) {
        if (head->search(_v) != nullptr)
            head->del(_v);
        return;
    }
    void print() {
        cout << "Start Printing\n";
        head->print(0);
        cout << "Finished\n";
    }
};

int main() {
    cout << "For add enter 0\nfor del enter 1\nfor search enter 2\n";
    bst T;
    while (true) {
        int n, j;
        cin >> j >> n;
        if (j == 0)
            T.push(n);
        if (j == 1)
            T.del(n);
        if (j == 2)
            cout << T.search(n) << '\n';
        T.print();
    }
    return 0;
}
