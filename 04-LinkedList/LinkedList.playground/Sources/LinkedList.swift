import Foundation

public struct LinkedList<Value> {
    public var head: Node<Value>?
    public var tail: Node<Value>?
    
    public init() {}
    
    public var isEmpty: Bool {
        return head == nil
    }
    
    public mutating func push(_ value: Value) {
        head = Node(value: value, next: head)
        if tail == nil {
            tail = head
        }
    }
    
    public mutating func append(_ value: Value) {
        guard !isEmpty else {
            push(value)
            return
        }

        tail!.next = Node(value: value)
        tail = tail!.next
    }
    
    public func node(atIndex: Int) -> Node<Value>? {
        var currNode = head
        var currIndex = 0
        
        while currNode != nil && currIndex < atIndex {
            currNode = currNode!.next
            currIndex += 1
        }
        
        if(currIndex == atIndex) {
            return currNode
        } else {
            return nil
        }
    }
    
    @discardableResult
    public mutating func insert(_ value: Value, after node: Node<Value>) -> Node<Value> {
        guard node !== tail else {
            append(value)
            return tail!
        }
        
        node.next = Node(value: value, next: node.next)
        return node.next!
    }
}

extension LinkedList: CustomStringConvertible {
    
    public var description: String {
        guard let head = head else {
            return "Empty LinkedList"
        }
        return String(describing: head)
    }
}
