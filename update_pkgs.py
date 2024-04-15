
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".github"))
from actions import main as github_action

def execute_main(pkg_name, versions, short_desc, homepage):
    # Delete
    os.environ["PKG_ACTION"] = "DELETE"
    os.environ["PKG_NAME"] = pkg_name
    github_action()
    print(f"Package {pkg_name} deleted")
    
    # Register
    os.environ["PKG_ACTION"] = "REGISTER"
    os.environ["PKG_NAME"] = pkg_name
    os.environ["PKG_VERSION"] = versions[0]
    os.environ["PKG_AUTHOR"] = "Nicolas Remond"
    os.environ["PKG_SHORT_DESC"] = short_desc
    os.environ["PKG_HOMEPAGE"] = homepage
    github_action()
    print(f"Package {pkg_name} registered")
    
    # Update
    for version in versions[1:]:
        os.environ["PKG_ACTION"] = "UPDATE"
        os.environ["PKG_NAME"] = pkg_name
        os.environ["PKG_VERSION"] = version
        github_action()
        print(f"Package {pkg_name} updated to version {version}")
    print(f"Package {pkg_name} done")



if __name__ == "__main__":
    
    # public-hello
    pkg_name = "public-hello"
    versions = ["0.1", "0.2", "0.3.dev0"]
    short_desc = 'A public github-hosted repo, with a dependency to another package.'
    homepage = 'https://github.com/adinrayana/public-hello'
    execute_main(pkg_name, versions, short_desc, homepage)
	
	# public-hello
    pkg_name = "IAM_Python_SDK"
    versions = ["0.1", "0.2", "0.3.dev0"]
    short_desc = 'A public github-hosted repo, with a dependency to another package.'
    homepage = 'https://github.com/hitachi-genai/platform-security-iam-python-sdk/tree/python-sdk-push'
    execute_main(pkg_name, versions, short_desc, homepage)
