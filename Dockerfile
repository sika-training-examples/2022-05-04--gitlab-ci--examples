FROM golang:1.18 as build
WORKDIR /build
COPY main.go .
ENV CGO_ENABLED=0
RUN go build -o hello main.go

FROM scratch
COPY --from=build /build/hello /hello
CMD ["/hello"]
