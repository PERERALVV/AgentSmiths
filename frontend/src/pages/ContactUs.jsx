import React, { useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import axios from "axios";
import Card from "../components/pages/Contact Us/Card";
import CustomToolbar from "../components/pages/Contact Us/CustomToolBar";
import send from "../images/send.png";
import phone from "../images/phone.png";
import email from "../images/email.png";
import location from "../images/location.png";
import {
  Container,
  ImageContainer,
  FormContainer,
  FormContent,
  Header,
  SubHeader,
  CardsContainer,
  Input,
  StyledButton,
  CompanyDetails,
} from "../styles/pages/ContactUsStyle";

const topics = [
  "Product Inquiry",
  "Support",
  "Feedback",
  "Billing",
  "Careers",
  "Partnerships",
  "Other",
];

const ContactUs = () => {
  const [selectedTopic, setSelectedTopic] = useState("");
  const [customTopic, setCustomTopic] = useState("");
  const [message, setMessage] = useState("");
  const [alignment, setAlignment] = useState("left");

  const handleSend = async () => {
    if (!selectedTopic || (!customTopic && selectedTopic === "Other")) {
      alert("Please select a topic.");
      return;
    }
    if (!message.trim()) {
      alert("Please enter a message.");
      return;
    }

    const topic = selectedTopic === "Other" ? customTopic : selectedTopic;

    try {
      await axios.post("http://localhost:8080/send-email", {
        topic,
        message,
        status: "unread",
      });
      alert("Email sent successfully!");
    } catch (error) {
      console.error(error);
      alert("Failed to send email.");
    }
  };

  const modules = {
    toolbar: {
      container: "#toolbar",
    },
  };

  const formats = [
    "header",
    "font",
    "size",
    "align",
    "bold",
    "italic",
    "underline",
    "strike",
    "blockquote",
    "code-block",
    "list",
    "bullet",
    "script",
    "indent",
    "link",
    "image",
    "video",
  ];

  return (
    <Container>
      <ImageContainer />
      <FormContainer>
        <FormContent>
          <Header>Contact Us</Header>
          <SubHeader>Select a Topic:</SubHeader>
          <CardsContainer>
            {topics.map((t) => (
              <Card
                key={t}
                selected={t === selectedTopic}
                onClick={() => setSelectedTopic(t)}
              >
                {t}
              </Card>
            ))}
          </CardsContainer>
          {selectedTopic === "Other" && (
            <Input
              type="text"
              placeholder="Please specify the topic"
              value={customTopic}
              onChange={(e) => setCustomTopic(e.target.value)}
            />
          )}
          <SubHeader>Tell us:</SubHeader>
          <CustomToolbar alignment={alignment} setAlignment={setAlignment} />
          <ReactQuill
            value={message}
            onChange={setMessage}
            modules={modules}
            formats={formats}
            style={{
              background: "#fff",
              color: "#333",
              borderRadius: "5px",
              marginBottom: "20px",
            }}
          />
          <StyledButton onClick={handleSend}>
            <img
              src={send}
              alt="Send"
              style={{ height: "20px", width: "auto", marginRight: "8px" }}
            />
            Send Message
          </StyledButton>
          <CompanyDetails>
            <p>
              <img
                src={phone}
                alt="phone"
                style={{ height: "20px", width: "auto", marginRight: "8px" }}
              />
              Phone:
              <a
                href="tel:+94774469039"
                style={{ textDecoration: "none", paddingLeft: "3px" }}
              >
                +94 774 469 039
              </a>
            </p>
            <p>
              <img
                src={email}
                alt="email"
                style={{ height: "20px", width: "auto", marginRight: "8px" }}
              />
              Email:
              <a
                href="mailto:contact@company.com"
                style={{ textDecoration: "none", paddingLeft: "3px" }}
              >
                contact@company.com
              </a>
            </p>
            <p>
              <img
                src={location}
                alt="location"
                style={{ height: "20px", width: "auto", marginRight: "8px" }}
              />
              Location: 123 Main Street, Anytown, USA
            </p>
          </CompanyDetails>
        </FormContent>
      </FormContainer>
    </Container>
  );
};

export default ContactUs;
