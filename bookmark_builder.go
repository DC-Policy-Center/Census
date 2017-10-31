package main

import (
    "bufio"
    "fmt"
    "os"
)

func check(x string) string{
  var y string;
  if x == "bill"{
    y = "BILL"
  } else {
    y = "not bill"
  }
  return y
}
func printSlice(s []string) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func main() {
	fmt.Println("Hello")

  scanner := bufio.NewScanner(os.Stdin)
  var s []string
  var text string
  var r string
  for text != "q" {  // break the loop if text == "q"
      fmt.Print("Enter your text: ")
      scanner.Scan()
      text = scanner.Text()
      r = check(text)
      fmt.Println(r)
      if text != "q" {
          fmt.Println("Your text was: ", text)
        }
      if text == "yes" {
        fmt.Printf("No...%v\n",text)
        }
      s = append(s,text)
      }
    printSlice(s)
    }
