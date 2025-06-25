# ------------------ Scalars ------------------
variable "name" {
  default = "Hari"
}

variable "age" {
  default = 25
}

variable "salary" {
  default = 100000
}

variable "is_devops_engineer" {
  default = true
}

variable "null_value" {
  default = null
}

# ------------------ Strings ------------------
output "quoted_strings" {
  value = {
    single_quoted = "Hello World"
    double_quoted = "Hello World"
    plain_string  = "Just a regular string"
  }
}

# ------------------ Multi-line ------------------
output "block_literal" {
  value = <<EOT
This is a block
literal string.
Line breaks are preserved.

EOT
}

output "block_folded" {
  value = "This is a folded block string. Line breaks are folded into spaces.
"
}

# ------------------ Lists ------------------
variable "skills" {
  type = list(string)
  default = ['Linux', 'Python', 'Terraform', 'Kubernetes', 'GitHub Actions']
}

variable "cloud_providers" {
  type = list(string)
  default = ['AWS', 'Azure', 'GCP']
}

# ------------------ Maps ------------------
variable "tools" {
  type = map(string)
  default = {
    
    terraform = "1.5.2"
    
    kubectl = "1.29"
    
    ansible = "2.15.3"
    
  }
}

# ------------------ Nested ------------------
resource "project" "example" {
  name = "DevOps Automation"

  team_lead = "Malli"
  members = [
    
    "Krishna",
    
    "Arjun",
    
  ]
}

# ------------------ List of Maps ------------------
resource "servers" "example" {
  count = 2
  name  = "web1"
  ip    = "192.168.0.1"
  role  = "frontend"
}

# ------------------ Anchors & Overrides ------------------
output "prod_settings" {
  value = {
    retries = 3
    timeout = 60
    debug   = True
  }
}

# ------------------ Boolean Variants ------------------
output "bools" {
  value = {
    yes_val   = true
    no_val    = false
    true_val  = true
    false_val = false
    on_val    = true
    off_val   = false
  }
}

# ------------------ Timestamps ------------------
output "deployment_time" {
  value = "2025-05-18 09:30:00+00:00"
}

output "created_on" {
  value = "2025-05-18"
}