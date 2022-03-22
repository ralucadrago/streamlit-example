import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn import metrics
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.tools
from statsmodels.stats.outliers_influence import variance_inflation_factor

st.title("Oh hey its an app")

st.text("Click the button")
button = st.button("Click meeee")
if button:
    st.title("Why would you do that? 😨")
    
st.text("Do you like making apps?")
yes = st.checkbox("Yes")
no = st.checkbox("No")

if yes and no:
    st.title("🙃")
elif yes:
    st.title("😊")
elif no:
    st.title("😭")

    
options = ["Lisa", "Lisa", "Lisa", "Lisa", "Lisa"]
st.text("Who's your favourite instructor?")
opinion = st.selectbox("Pick an instructor", options)
st.text("Congratulations, you selected {}".format(opinion))

st.text("Coffee is very important ☕️")
coffee = st.slider("How many coffees do you drink in a day?", 0, 10)
if coffee == 0:
    st.text("Weakling")
elif coffee < 3:
    st.text("Acceptable")
elif coffee < 6:
    st.text("Welcome to adult life")
else:
    st.text("I respect you")

st.title("Time for some data analysis 😍")
df = pd.read_csv("USA_Housing.csv")
df = df.rename(columns = {'Avg. Area Income': 'Income', 'Avg. Area House Age' : 'Age', 'Avg. Area Number of Rooms' : 'Rooms', 'Area Population' : 'Population'})

st.text("We are going to analyse the USA Housing dataset")
ye = st.button("Click to show data")
if ye:
    df
    
st.text("Let's explore some data 😄")
analysis = ["data frame shape", "pairplot", "heatmap", "summary statistics", "null value count"]
how = st.selectbox("What would you like to see?", analysis)
if how == "data frame shape":
    df.shape
elif how == "pairplot":
    fig = sns.pairplot(df) 
    st.pyplot(fig)
elif how == "heatmap":
    fig,ax = plt.subplots()
    ax = sns.heatmap(df.corr(), vmin = -1, vmax = 1, annot = True)
    st.pyplot(fig)
elif how == "summary statistics":
    df2 = pd.DataFrame(df.describe())
    df2
else:
    df3 =  pd.DataFrame(df.isnull().sum(), columns = ["null count"])
    df3

st.text("That data looks pretty nice, right?")
st.text("We're gonna fit a linear regression model on it!")
    
X = df[['Income', 'Age', 'Rooms', 'Population']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)
lin_reg = sm.OLS(y_train, X_train)
results = lin_reg.fit()
price_pred = list(results.predict(X_train))
price_pred2 = list(results.predict(X_test))

st.text("Here are the parameters generated by our model:")
df4  = pd.DataFrame(results.params, columns = ["parameters"])
df4
#results.summary()

rmse_train = np.round(statsmodels.tools.eval_measures.rmse(y_train, price_pred), 2)
rmse_test = np.round(statsmodels.tools.eval_measures.rmse(y_test, price_pred2), 2)
mae_train = np.round(statsmodels.tools.eval_measures.meanabs(y_train, price_pred), 2)
mae_test = np.round(statsmodels.tools.eval_measures.meanabs(y_test, price_pred2), 2)
mse_train = np.round(statsmodels.tools.eval_measures.mse(y_train, price_pred), 2)
mse_test = np.round(statsmodels.tools.eval_measures.mse(y_test, price_pred2), 2)

st.text("Time to evaluate the performance of our model")
st.text(f'The train RMSE is {rmse_train}, the test RMSE is {rmse_test}')
st.text(f'The train MAE is {mae_train}, the test MAE is {mae_test}')
st.text(f'The train MSE is {mse_train}, the test MSE is {mse_test}')

avg = y_train.mean()
avg2 = y_test.mean()
perc = np.round((rmse_train/avg)*100, 2)
perc2 = np.round((rmse_test/avg2)*100, 2)

st.text("Okay, but what does that mean? Let's add some context")
st.text(f'The train RMSE as a percentage of the mean is {perc}%,\nThe test RMSE as a percentage of the mean is {perc2}%')
st.text("Nice")

st.text("Now let's visualise our results 📈")

cols = ['Income', 'Age', 'Rooms', 'Population']
feature = st.selectbox("Which feature would you like to see the residuals of?", cols)
fig = plt.figure(figsize=(12,8))
fig = sm.graphics.plot_regress_exog(results, feature, fig=fig)
st.pyplot(fig)

st.text("Let's check if our residuals are normally distributed")
fig = sns.displot(y_test- price_pred2, kind = 'kde')
st.pyplot(fig)
st.text("Yes they are 🎉")

st.text("Now let's compare our predictions to the true values")
fig = plt.figure(figsize=(10, 6))
sns.regplot(x=y_test, y=price_pred2, line_kws={"color": "red"})
plt.ylabel('Predicted price',fontsize ='15')
plt.xlabel('Actual price',fontsize ='15')
plt.xticks(fontsize ='15')
plt.yticks(fontsize ='15')
plt.title('Actual vs Predicted price')
st.pyplot(fig)

st.text("Looking pretty great 😁")
