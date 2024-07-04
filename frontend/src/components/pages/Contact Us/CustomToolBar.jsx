// src/components/CustomToolbar.jsx
import React from "react";
import { ToolbarContainer } from "../../../styles/pages/ContactUsStyle";

const CustomToolbar = () => (
  <ToolbarContainer id="toolbar">
    <select className="ql-header" defaultValue="" onChange={(e) => e.persist()}>
      <option value="1" />
      <option value="2" />
      <option value="" />
    </select>
    <button className="ql-bold" />
    <button className="ql-italic" />
    <button className="ql-underline" />
    <button className="ql-strike" />
    <button className="ql-blockquote" />
    <button className="ql-code-block" />
    <button className="ql-list" value="ordered" />
    <button className="ql-list" value="bullet" />
    <button className="ql-indent" value="-1" />
    <button className="ql-indent" value="+1" />
    <button className="ql-align" value="" />
    <button className="ql-link" />
    <button className="ql-image" />
    <button className="ql-video" />
  </ToolbarContainer>
);

export default CustomToolbar;
