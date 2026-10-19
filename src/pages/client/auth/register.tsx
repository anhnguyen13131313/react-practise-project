import { Form, Input, Button, Divider } from "antd";
import { Link } from "react-router-dom";
import "./register.scss";
import { useState } from "react";
import { loginAPI } from "@/services/api";
interface FieldType {
  fullName: string;
  email: string;
  password: string;
  phone: string;
}

const RegisterPage = () => {
  const [isSubmit, setIsSubmit] = useState(false);
  const onFinish = async (values: FieldType) => {
    console.log(values);
    // const res = await loginAPI("admin@gmail.com", "123456");
    //success
  };

  return (
    <div className="register-page">
      <h2>Đăng Ký Tài Khoản</h2>
      <Form onFinish={onFinish} layout="vertical">
        <Form.Item<FieldType>
          label="Họ Tên"
          name="fullName"
          rules={[{ required: true, message: "Không được để trống!" }]}
        >
          <Input></Input>
        </Form.Item>
        <Form.Item<FieldType>
          label="Email"
          name="email"
          rules={[
            { required: true, message: "Không được để trống!" },
            { type: "email", message: "Vui lòng nhập đúng định dạng email!" },
          ]}
        >
          <Input></Input>
        </Form.Item>
        <Form.Item<FieldType>
          label="Mật khẩu"
          name="password"
          rules={[{ required: true, message: "Không được để trống!" }]}
        >
          <Input.Password></Input.Password>
        </Form.Item>
        <Form.Item<FieldType>
          label="Số điện thoại"
          name="phone"
          rules={[{ required: true, message: "Không được để trống!" }]}
        >
          <Input></Input>
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit" loading={isSubmit}>
            Đăng Ký
          </Button>
        </Form.Item>
      </Form>
      <Divider>Or</Divider>
      <div style={{ textAlign: "center" }}>
        Đã có tài khoản ? <Link to="/login">Đăng nhập</Link>
      </div>
    </div>
  );
};

export default RegisterPage;
