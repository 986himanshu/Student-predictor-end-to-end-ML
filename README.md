## End to End MAchine Learning Project
I am getting this error message on running web app on local enviornment:
CustomException
src.exception.CustomException: Error occured in python script name [C:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\src\pipeline\predict_pipeline.py] line number [17] error message['OneHotEncoder' object has no attribute '_drop_idx_after_grouping']

Traceback (most recent call last)
File "C:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\src\pipeline\predict_pipeline.py", line 17, in predict
data_scaled=preprocessor.transform(features)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\utils\_set_output.py", line 157, in wrapped
data_to_wrap = f(self, X, *args, **kwargs)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\compose\_column_transformer.py", line 827, in transform
Xs = self._fit_transform(
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\compose\_column_transformer.py", line 681, in _fit_transform
return Parallel(n_jobs=self.n_jobs)(
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\utils\parallel.py", line 65, in __call__
return super().__call__(iterable_with_config)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\joblib\parallel.py", line 1918, in __call__
return output if self.return_generator else list(output)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\joblib\parallel.py", line 1847, in _get_sequential_output
res = func(*args, **kwargs)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\utils\parallel.py", line 127, in __call__
return self.function(*args, **kwargs)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\pipeline.py", line 940, in _transform_one
res = transformer.transform(X)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\pipeline.py", line 696, in transform
Xt = transform.transform(Xt)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\utils\_set_output.py", line 157, in wrapped
data_to_wrap = f(self, X, *args, **kwargs)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\sklearn\preprocessing\_encoders.py", line 1036, in transform
if self._drop_idx_after_grouping is not None:
During handling of the above exception, another exception occurred:
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\flask\app.py", line 1498, in __call__
return self.wsgi_app(environ, start_response)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\flask\app.py", line 1476, in wsgi_app
response = self.handle_exception(e)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\flask\app.py", line 1473, in wsgi_app
response = self.full_dispatch_request()
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\flask\app.py", line 882, in full_dispatch_request
rv = self.handle_user_exception(e)
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\flask\app.py", line 880, in full_dispatch_request
rv = self.dispatch_request()
File "c:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\ML_deployed\lib\site-packages\flask\app.py", line 865, in dispatch_request
return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
File "C:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\app.py", line 37, in predict_datapoint
results=predict_pipeline.predict(pred_df)
File "C:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\src\pipeline\predict_pipeline.py", line 22, in predict
raise CustomException(e,sys)
src.exception.CustomException: Error occured in python script name [C:\Users\986hi\Student peformance predictor\Student-predictor-end-to-end-ML\src\pipeline\predict_pipeline.py] line number [17] error message['OneHotEncoder' object has no attribute '_drop_idx_after_grouping']
The debugger caught an exception in your WSGI application. You can now look at the traceback which led to the error.
To switch between the interactive traceback and the plaintext one, you can click on the "Traceback" headline. From the text traceback you can also create a paste of it. For code execution mouse-over the frame you want to debug and click on the console icon on the right side.

You can execute arbitrary Python code in the stack frames and there are some extra helpers available for introspection:

dump() shows all variables in the frame
dump(obj) dumps all that's known about the object