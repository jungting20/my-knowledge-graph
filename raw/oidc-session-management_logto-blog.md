# Implementing OIDC logout and session management: A complete guide

**Source:** https://blog.logto.io/oidc-session-management  
**Fetched:** 2026-04-10

---

## What is OIDC session management

OpenID Connect (OIDC) is a simple identity layer built on top of the OAuth 2.0 protocol. It allows clients to verify the identity of the end-user based on the authentication performed by the authorization server, as well as to obtain basic profile information about the end-user in an interoperable and REST-like manner.

OIDC is designed to be easy to use and implement, with a focus on simplicity and flexibility. It is widely used for single sign-on (SSO) and identity verification in web applications, mobile apps, and APIs.

Understanding authentication status and session management in OIDC is crucial. This article explains how OIDC sessions and user authentication status are managed in the context of interactions between the Identity Provider (IdP) and Relying Party (RP) or Service Provider (SP).

Key terms:
- **Identity Provider (IdP)**: The service that stores and authenticates user identities.
- **Service Provider (SP) / Relying Party (RP)**: A web application or service that relies on the IdP for user authentication.
- **Sign-in session / Authentication session**: The session established when a user logs in to the IdP.
- **Grant**: Centralized user authentication and authorization information generated and managed by the IdP.
- **Single Sign-On (SSO)**: A session service that permits a user to use one set of login credentials to access multiple applications.

---

## How does OIDC authentication flow work

1. The user accesses the web application (RP).
2. The RP redirects the user to the OIDC provider (IdP) for authentication.
3. The OIDC provider checks the user's sign-in session status. If no session exists or the session has expired, the user is prompted to sign in.
4. The user interacts with the sign-in page to get authenticated.
5. The sign-in page submits the interaction result to the OIDC provider.
6. The OIDC provider creates a new sign-in session and authentication grant for the user.
7. The OIDC provider redirects the user back to the RP with an authentication code (Authorization Code flow).
8. The RP receives the authentication code and exchanges it for tokens to access user information.

---

## What is RP sign-in session management

A sign-in session is established when a user logs in to the IdP. This session tracks the user's authentication status at the IdP. It typically includes:
- User's identity
- Authentication time
- Session expiration time

A session cookie is securely set in the user's browser to maintain the session state. This cookie is typically set with `HttpOnly` and `Secure` flags to prevent client-side access and ensure secure communication.

### One session for single RP

For each RP that the user accesses from different devices or browsers, a separate user sign-in session will be established. If the user logs out from one RP, the user will still be authenticated at other RPs until the session expires or the user logs out from all RPs.

### Centralized session for multiple RPs

The IdP maintains a consistent authentication state across multiple RPs as long as the user's session is active and the authentication requests come from the same user agent (device/browser). This enables SSO capabilities.

---

## Client-side authentication status

In OIDC, the client application (RP) relies on IdP-issued tokens to verify the user's identity and authentication/authorization status.

- **ID Token**: A short-lived token containing user information used to verify the authenticated user's identity.
- **Access Token**: A token that grants access to protected resources on behalf of the user. Can be short-lived or long-lived. If expired or cleared, the user may be considered "signed out" and need to re-authenticate.
- **Refresh Token**: If the `offline_access` scope is requested and granted, the client application may receive a refresh token. It allows extending the user's authentication status without requiring re-authentication. As long as the refresh token is valid, the user's authentication status can be maintained.

Token storage strategies:
- SPA applications: browser's local storage or session storage
- Web applications: server-side session data or cookies

---

## OIDC sign-out mechanisms

The sign-out process in OIDC is multi-faceted due to both centralized IdP-managed sign-in sessions and distributed client-side tokens.

### 1. Clear tokens and local session at the client side

The client application can remove stored tokens (ID token, access token, and refresh token) from the user's browser or memory. For web applications that manage their own sign-in sessions, additional steps include clearing the session cookie and any session data.

### 2. Clear centralized sign-in session at the IdP

As long as the IdP session is active, the user may be automatically re-authenticated even if client-side tokens have been cleared. To fully sign out:
- The client application (RP) initiates a sign-out request to the IdP.
- The RP redirects the user to the IdP's **end-session endpoint** to terminate the sign-in session and clear session cookies.
- Once the sign-in session is terminated, the IdP will prompt re-authentication for any linked RPs sharing the same session.

### 3. OIDC back-channel logout

When a user signs out from one RP, they may also want to be automatically signed out from all other RPs without additional user interaction. This is accomplished using the **back-channel logout** mechanism (OpenID Connect Back-Channel Logout 1.0).

- When the IdP receives a sign-out request from an RP, it clears the sign-in session and sends a back-channel logout notification to all RPs using the same session that have a registered back-channel logout endpoint.
- RPs receiving the notification perform necessary actions to clear the user's session and tokens, ensuring the user is fully signed out from all applications.
