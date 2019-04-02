import Foundation

public struct LinkedList<Value> {

    public var head: Node<Value>?
    public var tail: Node<Value>?
    
    public init() {}
    
    public var isEmpty: Bool {
        return head == nil
    }
    
    public mutating func push(_ val: Value) {
        head = Node(value: val, next: head)
        if tail == nil {
            tail = head
        }
    }
    
    public mutating func append(_ val: Value) {
        if isEmpty {
            push(val)
        } else {
            tail!.next = Node(value: val)
            tail = tail!.next
        }
    }
}

extension LinkedList: CustomStringConvertible {
    public var description: String {
        guard let head = head else {
            return "Empty List"
        }
        
        return String(describing: head)
    }

}
