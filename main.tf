resource "aws_instance" "web" {
  count         = 3
  ami           = "ami-0b0dcb5067f052a63"
  instance_type = "t2.micro"

  tags = {
    Name = "joseph-example-${terraform.workspace}-${count.index}"
  }
}