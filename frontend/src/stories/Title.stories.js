import { Title } from "../components";

export default {
  title: "Title",
  component: Title,
  argTypes: {
    onClick: {
      action: "onClick",
    },
  },
};

const Template = (args) => <Title {...args} />;

export const Uppercase = Template.bind({});
Uppercase.args = {
  children: "Hello",
  color: "#3c40c6",
  uppercase: true,
};

export const Lowercase = Template.bind({});
Lowercase.args = {
  children: "Hello",
  color: "#3c40c6",
  uppercase: false,
};
