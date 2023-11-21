<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Jakarta DBCP</title>
</head>
<body>

<%@ page import="java.sql.*, javax.sql.*, javax.naming.*" %>

<h2>Jakarta DBCP 를 이용한 DB univdb 연결 점검 프로그램</h2>
<%
try{
	InitialContext ctx = new InitialContext();
	DataSource ds = (DataSource) ctx.lookup("java:cmop/env/jdbc/mysql");
	Connection con = ds.getConnection();
	
	/*
	Context initCtx = new InitialContext();
	Context env = (Context) initCtx.lookup("java:comp/env/");
	DataSource ds = (DataSource) env.lookup("jdbc/mysql");
	Connection con = ds.getConnection()
	*/
	
	out.println("MySql 데이터베이스 univdb에 성공적으로 접속했습니다.");
	con.close();
} catch(Exception e){
	out.println(e.getMessage());
	e.printStackTrace();
}

%>
</body>
</html>
