resource "aws_instance" "instance1" {
  ami = ""
  instance_type = ""

}

resource "aws_instance" "name" {

  instance_type = "componet_1"
  ami = "12345"

  tags = {
    "subscription-id" = "prod-eus2"
    "environment" = "component-1"
  }
  
}

resource "aws_instance" "name" {

  instance_type = "componet_2"
  ami = "12345"

  tags = {
    "subscription-id" = "prod-eus2"
    "environment" = "component-2"
  }
  
}

resource "aws_instance" "name" {

  instance_type = "componet_3"
  ami = "12345"

  tags = {
    "subscription-id" = "prod-eus2"
    "environment" = "component-3"
  }
  
}

