package main

import (
    "bufio"
    "fmt"
    "os"
)

func write_link(census_variable string, variable_description string, series string, year string){
  var url string
  var output_fmt string
  url = fmt.Sprintf("https://factfinder.census.gov/bkmk/table/1.0/en/ACS/%v_%v/%v/0400000US11",year,series,census_variable)

  output_fmt = fmt.Sprintf("<li><a href ='%v'>%v</a>: %v</li>\n",url,census_variable,variable_description)

  fmt.Println("Writing formatted link\n    ",output_fmt)
  f, err := os.OpenFile("output.txt", os.O_APPEND|os.O_WRONLY, 0644)
  check(err)

  f.WriteString(output_fmt)
  defer f.Close()
}

func input_link_values(){
  scanner := bufio.NewScanner(os.Stdin)
  fmt.Print("Enter your census variable: \n")
  scanner.Scan()
  census_variable := scanner.Text()
  fmt.Print("Enter your census variable description: \n")
  scanner.Scan()
  variable_description := scanner.Text()
  series  := "5yr"
  fmt.Print("Currently only the ACS 5 year implemented (var 5yr)\n")
  fmt.Print("Enter your census year: ")
  scanner.Scan()
  year := scanner.Text()
  write_link(census_variable, variable_description, series, year)
}

func what_to_do()string{
  scanner := bufio.NewScanner(os.Stdin)
  fmt.Println("What would you like to do??  \n")
  fmt.Println("\tadd:  add more links\n\tclear:  clear output\n\tq:  quit")
  scanner.Scan()
  action_variable := scanner.Text()

  return action_variable
}


func check(e error) {
    if e != nil {
        panic(e)
    }
}

func create_output(){
  os.Create("output.txt")
}
func remove_output(){
  os.Remove("output.txt")
}

func remove_create_output(){
  remove_output()
  create_output()
}

func main() {

	fmt.Println("Hello, welcome to the census link builder tool")
  action_variable := "continue"
  action_variable = what_to_do()

  for action_variable != "q" {  // break the loop if text == "q"
    if action_variable == "add"{
      input_link_values()
      action_variable = what_to_do()

      if action_variable == "q" {
          fmt.Println("\n\n\t\t\tQuitting, thank you\n\n ")
        }

    } else if action_variable == "clear"{
      fmt.Println("Clearing output file...\n")
      remove_create_output()
      action_variable = what_to_do()
  }
  }
}
