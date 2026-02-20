if prediction[0]==0:
        result = " You don't have any Anemic Disease"
    elif prediction[0]==1:
        result = " You have Anemic Disease"

    text = "Hence, based on calculation:"
    return render_template('predict.html', prediction_text = text+st