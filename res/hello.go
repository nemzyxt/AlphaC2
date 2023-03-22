package main

import (
	"os"
	"path/filepath"
)

func main() {
	home, _ := os.UserHomeDir()
	desktop := filepath.Join(home, "Desktop")
	os.Chdir(desktop)
	file, _ := os.Create("README.md")
	file.Write([]byte("Hello friend"))
}