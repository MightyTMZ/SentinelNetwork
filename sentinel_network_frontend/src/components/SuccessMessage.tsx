interface Props {
  message: string;
  bold: boolean;
}

const SuccessMessage = (props: Props) => {
  return (
    <div className="text-success">
      {props.bold ? <strong>{props.message}</strong> : props.message}
    </div>
  );
};

export default SuccessMessage;
