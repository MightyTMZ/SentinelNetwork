interface Props {
  message: string;
  bold: boolean;
}

const ErrorMessage = (props: Props) => {
  return (
    <div className="text-danger">
      {props.bold ? <strong>{props.message}</strong> : props.message}
    </div>
  );
};

export default ErrorMessage;
