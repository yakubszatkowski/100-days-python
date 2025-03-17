

class ChatGPT_API:
    def __init__(self):
        pass

    def input(focus_input, source_text, cloze_number=2, word_count=40, output_density=30):
        message_output = f'''
Review Text: "{source_text.replace('\n', ' ')} "

Task: 
- Create concise and direct statements from the provided text that focus on {focus_input}. 
- Add cloze deletions to these statements using Anki cloze deletion mark-up. Ensure that each statement is clearly written, easily understandable, and adheres to the specified formatting and reference criteria.

Formatting Criteria: 
- Construct a table with three columns: "Statements", "Notes", and "Number".
- Each row of the "Statements" column should contain a single statement written in Anki cloze deletion mark-up. Prioritize information about {focus_input}.
- Each row of the "Notes" column should provide additional information for the corresponding "Statement". Do not restate or summarize information already present in the "Statment". Information in the notes section should be sourced from the text.
- The "Number" column should serve to number each row, facilitating feedback.

Reference Criteria for each "Statement":
- Restrict each statement to {cloze_number} cloze deletions. If necessary, add 1-2 more cloze deletions, but they can only be either a cloze1 or cloze2 deletion.
- Limit the word count of each state                     ment to less than {word_count} words.
- Keep the text within the cloze deletions limited to one or two key words.
- Each statement must be able to stand alone. Include the subject of the statement somewhere in the text.
- Keep ONLY simple, direct, cloze deletion statements in the "Statements" column. Keep any additional explanatory information in the "Notes" column.
- Try to cover every aspect of the reviewed text in the flashcards, make at least {output_density} of them
        ''' + \
        r'''
Example Chatbot Response: 
| Statements | Notes | Number |
| --- | --- | --- |
| {{c1::Necrosis}} in pancreatitis is identified by lack of contrast enhancement after bolus contrast administration. | Necrotizing pancreatitis is associated with increased severity of disease and increased risk of death. | 1 |
| Acute {{c1::peripancreatic fluid collections}} are non-encapsulated aggregations of fluid in the pancreatic bed and retroperitoneum.  |  | 2 |
        '''

        return message_output 


output = ChatGPT_API.input(
    "AWS, Amazon Web Services",
    r'''IAM Section www.datacumulus.com IAM: Users & Groups • IAM = Identity and Access Management, Global service • Root account created by default, shouldn’t be used or shared • Users are people within your organization, and can be  
grouped • Groups only contain users, not other groups • Users don’t have to belong to a group, and user can belong to multiple groups Alice Bob Charles David Edward Group: Developers Group Group: Operations Audit Team Fred www.datacumulus.com IAM: Permissions • Users or Groups can be assigned JSON documents called policies • These policies define the permissions of the users • In AWS you apply the least privilege principle: don’t give more permissions than a user needs { "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:Describe*", "Resource": "*" }, { "Effect": "Allow", "Action": "elasticloadbalancing:Describe*", "Resource": "*" }, { "Effect": "Allow", "Action": [ "cloudwatch:ListMetrics", "cloudwatch:GetMetricStatistics", "cloudwatch:Describe*" ], "Resource": "*" } ] } www.datacumulus.com IAM Policies inheritance Alice Bob Charles David Edward Developers Operations Audit Team Fred inline www.datacumulus.com IAM Policies Structure • Consists of • Version: policy language version, always include “2012-10- 17” • Id: an identifier for the policy (optional) • Statement: one or more individual statements (required) • Statements consists of • Sid: an identifier for the statement (optional) • Effect: whether the statement allows or denies access (Allow, Deny) • Principal: account/user/role to which this policy applied to • Action: list of actions this policy allows or denies • Resource: list of resources to which the actions applied to • Condition: conditions for when this policy is in effect (optional) www.datacumulus.com IAM – Password Policy • Strong passwords = higher security for 
 your account • In AWS, you can setup a password policy: • Set a minimum password length • Require specific character types: • including uppercase letters • lowercase letters • numbers • non-alphanumeric characters • Allow all IAM users to change their own passwords • Require users to change their password after some time (password expiration) • Prevent password re-use www.datacumulus.com Multi Factor Authentication - MFA • Users have access to your account and can possibly change configurations or delete resources in your AWS account • You want to protect 
your Root Accounts and IAM users • MFA = password you know + security device you own • Main benefit of MFA: if a password is stolen or hacked, the account is not compromised Alice Password + => Successful login www.datacumulus.com MFA devices options in  AWS Virtual MFA device Google Authenticator (phone only) Authy (phone only) Universal 2nd Factor (U2F) Security Key YubiKey by Yubico (3rd party) Support for multiple tokens on a single device. Support for multiple root and IAM users using a single security key www.datacumulus.com MFA devices options in AWS Hardware Key Fob MFA Device Provided by Gemalto (3rd party) Hardware Key Fob MFA Device for AWS GovCloud (US) Provided by SurePassID (3rd party) www.datacumulus.com How can users access AWS ? • To  access AWS, you have three options: • AWS Management Console (protected by password + MFA) • AWS Command Line Interface (CLI): protected by access keys • AWS Software Developer Kit (SDK) - for code: protected by access keys • Access Keys are generated through the AWS Console • Users manage their own access keys • Access Keys are secret, just like a password. Don’t share them • Access Key ID ~= username • Secret Access Key ~= password www.datacumulus.com Example (Fake) Access Keys • Access key ID: AKIASK4E37PV4983d6C • Secret Access Key: AZPN3zojWozWCndIjhB0Unh8239a1bzbzO5fqqkZq • Remember: don’t share your access www.datacumulus.com What’s the AWS CLI? • A tool that enables you to interact with AWS services using commands in your command-line shell • Direct access to the public APIs of AWS services • You can develop scripts to manage your resources • It’s open-source https://github.com/aws/aws-cli • Alternative to using AWS Management Console www.datacumulus.com What’s the AWS SDK? • AWS Software Development Kit (AWS SDK) • Language-specific APIs (set of libraries) • Enables you to access and manage AWS services programmatically • Embedded within your application • Supports • SDKs (JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++) • Mobile SDKs (Android, iOS, …) • IoT Device SDKs (Embedded C, Arduino, …) • Example: AWS CLI is built on AWS SDK for Python AWS SDK Your Application www.datacumulus.com IAM Roles for Services • Some AWS service will need to perform actions on your behalf • To do so, we will assign permissions to AWS services with IAM Roles • Common roles: • EC2 Instance Roles •  Lambda Function Roles • Roles for CloudFormation EC2 Instance (virtual server) IAM Role Access AWS www.datacumulus.com IAM Security Tools • IAM Credentials Report (account-level) • a report that lists all your account's users and the status of their various credentials • IAM Access Advisor (user-level) • Access advisor shows the service permissions granted to a user and when those services were last accessed. • You can use this information to revise your policies. www.datacumulus.com IAM Guidelines &  Best Practices • Don’t use the root account except for AWS account setup • One physical user = One AWS user • Assign users to groups and assign permissions to groups • Create a strong password policy • Use and enforce the use of Multi Factor Authentication (MFA) • Create and use Roles for giving permissions to AWS services • Use Access Keys for Programmatic Access (CLI / SDK) • Audit permissions of your account using IAM Credentials Report & IAM Access Advisor • Never share IAM users & Access www.datacumulus.com Shared Responsibility Model for IAM • Infrastructure (global network security) • Configuration and vulnerability analysis • Compliance validation You • Users, Groups, Roles, Policies management and monitoring • Enable MFA on all accounts • Rotate all your keys often • Use IAM tools to apply appropriate permissions • Analyze access patterns & review permissions www.datacumulus.com IAM Section – Summary • Users: mapped to a physical user, has a password for AWS Console • Groups: contains users only • Policies: JSON document that outlines permissions for users or groups • Roles: for EC2 instances or AWS services • Security: MFA + Password Policy • AWS CLI: manage your AWS services using the command-line • AWS SDK: manage your AWS services using a programming language • Access Keys: access AWS using the CLI or SDK • Audit: IAM Credential Reports & IAM Access Advisor
'''
    )

print(output)
