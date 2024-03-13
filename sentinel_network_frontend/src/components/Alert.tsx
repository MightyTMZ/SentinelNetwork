interface Props {
  message: string;
  color: string;
}

// this component is unfinished

const Alert = (props: Props) => {
  // Define the base class for the alert
  const baseClass = "alert alert-dismissible fade show";

  // Construct the className based on the color prop
  const className = `${baseClass} alert-${props.color}`;

  return (
    <div className={className} role="alert">
      {props.message}
      <button
        type="button"
        className="close"
        data-dismiss="alert"
        aria-label="Close"
      >
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
  );
};

export default Alert;
