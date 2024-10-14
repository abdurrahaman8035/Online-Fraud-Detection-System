import json
import requests
import streamlit as st

# App title
st.title("Online Fraud Detection System using Machine Learning")
st.text("PROJECT BY: AHMAD ABDU GOGE")

#some image
st.image("img/credit_card_fraud.jpg")

# Description
st.write(
    """
    ## About
    
    With the growth of e-commerce websites, people and financial companies rely on online services
    to carry out their transactions that have led to an exponential increase in the credit card frauds.
    Fraudulent credit card transactions lead to a loss of huge amount of money. The design of an
    effective fraud detection system is necessary in order to reduce the losses incurred by the
    customers and financial companies. 

    """
)





















































###################### Funtions to transform categorical variable #############################################
def type_transaction(content):
    if content == "PAYMENT":
        content = 0
    elif content == "CASH_OUT":
        content = 2
    elif content == "DEBIT":
        content = 3
    elif content == "CASH_IN":
        content = 4
    return content

######################################### Input elements #############################################################
st.sidebar.header("Input user and transaction information")

# User data
sender_name = st.sidebar.text_input(" Sender Name ID")
receiver_name = st.sidebar.text_input(" Receiver Name ID")

## Transaction information
type_lebels = ("PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN")
type = st.sidebar.selectbox(" Type of transaction", type_lebels)

step = st.sidebar.slider("Number of Hours it took the Transaction to complete:", min_value = 0, max_value = 744)

amount = st.sidebar.number_input("Amount in Naira",min_value=0, max_value=200000000)
oldbalanceorg = st.sidebar.number_input("""Sender Balance Before Transaction was made""",min_value=0, max_value=1000000)
newbalanceorg = st.sidebar.number_input("""Sender Balance After Transaction was made""",min_value=0, max_value=1000000)
oldbalancedest = st.sidebar.number_input("""Recipient Balance Before Transaction was made""",min_value=0, max_value=1000000)
newbalancedest = st.sidebar.number_input("""Recipient Balance After Transaction was made""",min_value=0, max_value=1000000)
## flag 



result_button = st.button("Detect Result")

if result_button:

    ## Features
    data = {
        "step": step,
        "type": type_transaction(type),
        "amount": amount,
        "oldbalanceOrg": oldbalanceorg,
        "newbalanceOrg": newbalanceorg,
        "oldbalanceDest": oldbalancedest,
        "newbalancedDest": newbalancedest
    }

    
    st.write("""## **Prediction**""")


if result_button:
    # Transaction details
    st.write(
        f""" 
        ## **Transaction Details**

        #### **User information**:

        Sender Name(ID): {sender_name}\n
        Receiver Name(ID): {receiver_name}

        #### **Transaction information**:

        Number of Hours it took to complete: {step}\n
        Type of Transaction: {type}\n
        Amount Sent: N{amount}\n
        Sender Balance Before Transaction: N{oldbalanceorg}\n
        Sender Balance After Transaction: {newbalanceorg}\n
        Recipient Balance Before Transaction: N{oldbalancedest}\n
        Recipient Balance After Transaction: N{newbalancedest}\n
        
        """
    )

    

    # Add if statements to check for fraud conditions
    if sender_name == '' or receiver_name == '':
        st.write("Error! Please input Transaction ID or Names of Sender and Receiver!")
    else:
        # Condition 1: Check if the amount exceeds a high threshold (e.g., N100,000,000)
        if amount > 100000000:
            st.write(f"""### The **'{type}'** transaction between {sender_name} and {receiver_name} is predicted to be **fraudulent**.""")
            st.warning("⚠️ This transaction is flagged as fraudulent due to a large amount.")
        
        # Condition 2: Check if the sender's balance after the transaction is negative (suspicious)
        elif newbalanceorg < 0:
            st.write(f"""### The **'{type}'** transaction between {sender_name} and {receiver_name} is predicted to be **fraudulent**.""")
            st.warning("⚠️ This transaction is flagged as fraudulent due to the sender having a negative balance after the transaction.")
        
        # Condition 3: Check if the transaction is of a suspicious type (e.g., CASH_OUT)
        elif type == "CASH_OUT" and amount > 5000000:
            st.write(f"""### The **'{type}'** transaction between {sender_name} and {receiver_name} is predicted to be **fraudulent**.""")
            st.warning("⚠️ This transaction is flagged as fraudulent due to a large cash out amount.")
        
        # Condition 4: Check if the recipient's balance increases suspiciously
        elif newbalancedest - oldbalancedest > amount:
            st.write(f"""### The **'{type}'** transaction between {sender_name} and {receiver_name} is predicted to be **fraudulent**.""")
            st.warning("⚠️ This transaction is flagged as fraudulent due to an unexpected large increase in the recipient's balance.")
        
        # Condition 5: General safe case for legitimate transactions
        else:
            st.write(f"""### The **'{type}'** transaction between {sender_name} and {receiver_name} is predicted to be **non-fraudulent**.""")
            st.success("✅ This transaction appears legitimate.")

