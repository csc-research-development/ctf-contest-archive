export class ApiError extends Error {
	constructor(message, status = 500) {
		super(message)
		this.name = 'ApiError'
		this.status = status
	}
}

export class BadRequestError extends ApiError {
	constructor(message) {
		super(message, 400)
		this.name = 'BadRequestError'
	}
}

export class ForbiddenError extends ApiError {
	constructor(message) {
		super(message, 403)
		this.name = 'ForbiddenError'
	}
}

export class UnauthorizedError extends ApiError {
	constructor(message) {
		super(message, 401)
		this.name = 'UnauthorizedError'
	}
}

export class NotFoundError extends ApiError {
	constructor(message) {
		super(message, 404)
		this.name = 'NotFoundError'
	}
}
