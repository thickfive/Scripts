func main() -> Void {
    defer {
        function(1)
    }
    function(2)
    return function(3)
}

func function(_ i: Int) {
    print("function", i)  
}

main()
// function 2
// function 3
// function 1