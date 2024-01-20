import smtplib, ssl



class Solution:
    def send_mail(self, to, sub, msg):
        port = 465  # For SSL
        password = input("Type your password and press enter: ")

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP("smtp.gmail.com", port) as server:
            server.login("abc@gmail.com", password)
            server.sendmail("abc@gmail.com", "to", msg=msg)

if __name__ == "__main__":
    sol = Solution()
    sol.send_mail('anc@gmail.com', 'py-sub', 'py-msg')