resource "aws_instance" "main" {
    instance_type = "t2.micro"
    ami = "ami01234"
}