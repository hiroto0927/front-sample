import { memo } from "react";

const ToggleSwitch = memo(function ToggleSwitch(props: {
  onChage?: React.ChangeEventHandler<HTMLInputElement>;
  isCheck?: boolean;
}) {
  return (
    <label>
      <input
        v-model="isCheck"
        type="checkbox"
        className="peer sr-only"
        onChange={props.onChage}
        checked={props.isCheck}
      />
      <span
        className="block w-[2em] cursor-pointer rounded-full bg-gray-500 
      p-[1px] after:block after:h-[1em] after:w-[1em] after:rounded-full 
      after:bg-white after:transition peer-checked:bg-blue-500 
      peer-checked:after:translate-x-[calc(100%-2px)]"
      ></span>
    </label>
  );
});

export default ToggleSwitch;
