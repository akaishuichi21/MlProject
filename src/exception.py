import sys
import logging

def errorMessageDetail(error, errorDetail:sys):
    _,_,exc_tb = errorDetail.exc_info()
    fileName = exc_tb.tb_frame.f_code.co_filename
    line = exc_tb.tb_lineno
    errorMessage = "error has occured at [{0}], in line [{1}], with the following error message: [{2}]".format(
        fileName,
        line,
        str(error)
    )

    return errorMessage


    

class CustomException(Exception):
    def __init__(self, errorMessage, errorDetail:sys):
        super().__init__(errorMessage)
        self.errorMessage=errorMessageDetail(errorMessage, errorDetail)

    def __str__(self):
        return self.errorMessage
    


if __name__ == "__main__":
    try:

        1/0

    except Exception as e:
        logging.info("division by zero exception!!!!")
        raise CustomException(e, sys)
