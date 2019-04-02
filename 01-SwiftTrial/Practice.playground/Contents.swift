import UIKit

let hetrogenousArray: [Any] = [1, "Ashutosh", 21, "Sonu"]

hetrogenousArray.forEach { (val) in
    print("The value is \(val)")
}

let nums = [7, 11, 13, 17, 19, 23]

nums.forEach { (num) in
    print("Some primary numbers are \(num)")
}

var people = ["Sonu", "Rupi", "Rinku", "Pinki", "Minu"]

people.append("Charles")

print("Array is now: \(people)")
people.insert("Bobby", at: 1)

print("Array is now: \(people)")

let dict = ["amal": 4.5, "jonathan" : 3.5, "fatima" : 4, "ellen" : 4, "bruno" : 2]

for (key, val) in dict {
    print("The value of key \(key) is \(val)")
}

let numbers = [1, 3, 56, 66, 68, 80, 99, 105, 450]

func doesContain(nums: [Int], val: Int) -> Bool {
    var start = 0
    var end = nums.count - 1
    var mid = 0
    while start <= end {
        mid = (start + end) / 2
        if(nums[mid] == val) {
            return true
        } else if nums[mid] < val {
            start = mid + 1
        } else {
            end = mid - 1
        }
    }
    return false
}

print("Does contain: \(doesContain(nums: numbers, val: 48))")
print("Does contain: \(doesContain(nums: numbers, val: 450))")
print("Does contain: \(doesContain(nums: numbers, val: 1))")
print("Does contain: \(doesContain(nums: numbers, val: 37))")
print("Does contain: \(doesContain(nums: numbers, val: 66))")


